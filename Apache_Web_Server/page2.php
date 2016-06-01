<!DOCTYPE html>
<html>
<head>
<link type="text/css" rel='stylesheet' href='style.css'/>
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<link href="http://s3.amazonaws.com/codecademy-content/courses/ltp2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="jumbotron" style="background-color:black">
	<p style='font-size:30px; color:white; text-align:center;'> Prime Factorization </p>
</div>
<div class="container">
	
</div>
<div class="container">
  <div class="jumbotron" style="background-color:black">
    <h1></h1>
    	<p style="color: orange; text-align:center">
		<?php
	
		/*
		if (!isset($_POST['numpis']) && empty($_POST['num'])){
			echo "<p style='color: orange; text-align:center'>
				Please enter a number. Please choose a cluster size.
			</p>";
		}
		else if(!isset($_POST['numpis']) && !empty($_POST['num'])){
			echo "<p style='color: orange; text-align:center'>
				Please choose a cluster size.
			</p>";
		}
		else if(isset($_POST['numpis']) && empty($_POST['num'])){
			echo "<p style='color: orange; text-align:center'>
				Please enter a number.
			</p>";
		}
		else 
		*/
		if(isset($_POST['numpis'])){ 
			$comp_num = $_POST['num'];
			$cluster_size = $_POST['numpis'];
			
			//echo $cluster_size;
			switch($cluster_size){
				case "1":
					echo "1";
					echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
					break;
				case "2":
					echo "2";
					echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
					break;
				case "3":
					echo "3";
					echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
					break;
				case "4":
					echo "4";
					echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
					break;
				case "5":
					echo "5";
					echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
					break;
				default:
					echo "...";

			}
			//echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
			//echo exec('python /var/www/html/test/test.py ' . $comp_num);
		} 
		
	
		?>
	</p>	
  </div>
  <div class="jumbotron" style="background-color:white">
  	<p style="color: black; text-align:center">
	Click <a href = "page1.html"> here </a> to try again.
	</p>
  </div>	
</div>
<div class="footer navbar-fixed-bottom">
  <p style='font-size:20px; text-align:center;'>Jacob Morra &copy 2016</p>
</div>
<?php
$r = 'python ./test.py';
exec($r);

$im = imagecreatefrompng("img.png");
header('Content-Type: image/png');
imagepng($im);
imagedestroy($im);
?>
</body>
</html>

