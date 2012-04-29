from django.http import HttpResponse

def sumilux(request):
	html = """<!doctype html>
			<html lang = "en">
				<head>
					<meta charset = "utf-8"/>
					<title>Django view to output a html page</title>
					<style>
						#wrapper{	width : 90%;
								margin : 0 auto;
								}
						#aside{	width : 30%; 
								float : right;
								background-color :#3399FF ;
								padding : 15px;
								border-radius : 10px;
								}
						#content{
								width : 60%;
								float :left;
								border : 2px blue;
								background-color : #CC66CC;
								padding : 15px;
								border-radius : 10px;
								}
						
					</style>
				</head>

				<body>
					<div id = "wrapper">
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
					</div>	
				</body>
			</html>
		"""			
					
					
					
					
					
					
					
	return HttpResponse(html)				