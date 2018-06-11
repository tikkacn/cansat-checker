from flask import Flask
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
	the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

	r = requests.get('http://www.cansatcompetition.com/mission.html')

	reference = """
<!DOCTYPE HTML>
<html>

<head>
  <title>CanSat Competition</title>
  <meta name="description" content="Cansat Competition" />
  <meta name="keywords" content="cansat, competition, university, satellite, pdr, cdr, high power rockets" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <link rel="stylesheet" type="text/css" href="css/style.css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>

<body>
  <div id="main">
    <header>
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1><a href="index.html">CanSat Competition</a></h1>
          <h2>Mission</h2>
        </div>
      </div>
      <nav>
        <div id="menu_container">
          <ul class="sf-menu" id="nav">
            <li><a href="index.html">Home</a></li>
            <li><a href="mission.html">Mission</a></li>
            <li><a href="teams.html">Teams</a></li>
	    <li><a href="winners.html">2017 Winners</a></li>
	    <li><a href="photos.html">Photos</a></li>
			<li><a href="documents.html">Documents</a></li>
             <li><a href="mailto:cansatcompetition@gmail.com?subject=CanSat Competition">Contact Us</a></li>
          </ul>
        </div>
      </nav>
    </header>
    <div id="site_content">
      <div id="sidebar_container">
		<div class="sidebar">
			<h2>Documents</h2>
<br><br>
 <br>PDR will be more extensive since the top 40 teams will be selected after PDR.
			<h2><a href="docs/mission_guide_2018_r20171020_r1.4.pdf">Mission Guide - Oct 20, 2017</a></h2> 
			<h2><a href="docs/Cansat 2018 PDR Outline v1.2.pptx">PDR Outline - Jan 25, 2018</a></h2>
			<h2><a href="docs/Cansat 2018 CDR Outline v1.2.pptx">CDR Outline - Mar 19, 2018</a></h2>
			<h2><a href="docs/Scoresheet Template 2018.xlsx">Competition Score Sheet</a></h2>
			<h2><a href="docs/Cansat_environmental_tests_r1.3.pdf">Environmental Test Guide</a></h2>
			<h2><a href="docs/mission_operations_manual_2016.doc">Mission Operations Manual</a></h2>
			<h2><a href="docs/pfr_outline_2018.pdf">Post Flight Review Outline</a></h2>
        </div>
      </div>
      <div class="content">
        <h1>Introduction</h1>
<p>The 2018 mission simulates a space probe (CanSat) entering a planetary atmosphere. The probe shall carry a single large hen's egg. The egg must survive all portions of flight. The operation sequence shall be:
<p>1. The probe is launched to an altitude of 670 meters to 725 meters and then deployed from the rocket. Orientation of deployment is not controlled and is most definitely violent.
<p>2. Once deployed, the probe shall open an aero-braking heat shield. The descent rate shall be kept at 10 to 30 meters/sec. The aero-braking probe must maintain a stable orientation with the heat shield facing the direction of descent during descent. Tumbling is not allowed. Active control surfaces or other non pyrotechnic mechanisms can be used to maintain orientation.
<p>3. At an altitude of 300 meters, the probe shall release the aero-braking heat shield and simultaneously deploy a parachute to reduce the descent rate of 5 meters/sec.
<p>4. The probe shall land leaving the egg intact.
<p>The probe shall include sensors for tracking altitude using air pressure, external temperature, battery voltage and GPS position. A compartment shall be included to hold a large hen's egg. The egg will simulate a delicate instrument.


      </div>
    </div>
    <div id="scroll">
      <a title="Scroll to the top" class="top" href="#"><img src="images/top.png" alt="top" /></a>
    </div>
    <footer>
     
      <p><a href="index.html">Home</a> | <a href="mission.html">Mission</a> | <a href="teams.html">Teams</a> | <a href="mailto:cansatcompetition@gmail.com?subject=CanSat Competition">Contact Us</a></p>
      <p>Copyright &copy; CSS3_contrast | <a href="http://www.css3templates.co.uk">design from css3templates.co.uk</a></p>
    </footer>
  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.js"></script>
  <script type="text/javascript" src="js/jquery.easing-sooper.js"></script>
  <script type="text/javascript" src="js/jquery.sooperfish.js"></script>
  <script type="text/javascript">
    $(document).ready(function() {
      $('ul.sf-menu').sooperfish();
      $('.top').click(function() {$('html, body').animate({scrollTop:0}, 'fast'); return false;});
    });
  </script>
</body>
</html>
"""
	print(r.text)
	print(reference)
	print(r.text == reference)

	return """
	<h1>Hello heroku</h1>
	<p>It is currently {time}.</p>

	<img src="http://loremflickr.com/600/400">

	""".format(time=the_time)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)




