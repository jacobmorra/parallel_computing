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
	
		if (isset($_POST['numpis']) && !empty($_POST['num'])){
		//echo "2";
		$comp_num = $_POST['num'];
		$cluster_size = $_POST['numpis'];
		
		//echo "Composite Number is " . $comp_num;
		//echo "Cluster Size is " . $cluster_size;
	
		//echo exec('python /var/www/html/test/test.py ' . $comp_num . ' ' . $cluster_size);
		echo exec('python /var/www/html/test/test.py ' . $comp_num);
		} 
	
		?>
	</p>
	 	
  </div>
</div>
<footer>
  <p style='font-size:20px; text-align:center;'>Jacob Morra &copy 2016</p>
</footer>
</body>
</html>

