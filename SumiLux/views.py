from django.http import HttpResponse

def sumilux(request):
	html = """<!doctype html>
			<html lang = "en">
				<head>
					<meta charset = "utf-8"/>
					<title>Django view to output a html page</title>
				</head>

				<body>
					<div id = "aside">
						<p>Lorem ipsum dolor sit amet.</p>
					</div>
					<div id = "content">
						<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
						<p>Fusce placerat auctor mauris, quis condimentum augue dapibus nec.</p>
						<p>Sed nec orci et lacus elementum malesuada.</p>
						<p>Donec quis libero a sem vulputate varius.</p>
						<p>Donec fermentum viverra sem, a porta turpis accumsan in.</p>
					</div>
				</body>
			</html>
		"""			
					
					
					
					
					
					
					
	return HttpResponse(html)				