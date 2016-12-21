from django.shortcuts import render
from django.http import HttpResponse

from clarifai.rest import ClarifaiApp
from santa_search.models import Image

app = ClarifaiApp()

def tag_search(request):
	query = request.POST.get('tag')
	if query:
		img_list = Image.objects.filter(tags = query)

def store_images(image_url):
	response = app.tag_urls([image_url])
	outputs = response.get('outputs')
	data = {}
	tags_list = []
	for output in outputs:
		data.update(output.get("data"))
	tags_id = data.get('concepts')
	for tag_id in tags_id:
		tags_list.append(str(tag_id.get('name')))
	#Store attributes in redis Object
	return Image.objects.get_or_create(url=image_url, tags = tags_list)

def load_images(request):
	from ImgSearch.settings.base import BASE_DIR
	from os.path import join
	fp = open(join(BASE_DIR, 'static/images_corpus.txt'))
	for line in fp.readlines():
		store_images(line)
	return HttpResponse(status=201)
