import get_data

def frac_time():
	urls, reqmap = get_data.getData()

	reqmap = sorted(reqmap, key=lambda x: return x['totalTime'])

	display_urls = reqmap[:10]
	return display_urls


