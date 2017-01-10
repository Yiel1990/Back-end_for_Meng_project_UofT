<?php  
  
echo "<html><head><title>Picture</title></head><body bgcolor=000000><center><font size=2 color=red>";
$page=$_GET['page']; 
  
$max=5;
  
$path="./uploads";  
  
$handle = opendir($path); 
  
    while (false !== ($file = readdir($handle))) {  
  
      list($filesname,$kzm)=explode(".",$file);
  
        if($kzm=="gif" or $kzm=="jpg" or $kzm=="JPG") { 
  
           if (!is_dir('./'.$file)) {  
  
             $array[]=$file;  
  
             $i++; 
  
            }  
  
          }  
  
    }  
  
for ($j=$max*$page;$j<($max*$page+$max)&&$j<$i;++$j){ 
  
echo "<a href=".$path."/".$array[$j]."><img width=150 height=110 src=".$path."/".$array[$j]."></a><br>";  
  
}  
  
$Previous_page=$page-1;  
  
$next_page=$page+1;  
  
if ($Previous_page<0){  
  
    echo "prev";  
  
    echo "<a href=?page=$next_page>next</a>";  
  
}  
  
    else if ($page<=$i/$max){  
  
      echo "<a href=?page=$Previous_page>prev</a>";  
  
      echo "<a href=?page=$next_page>next</a>";}  
  
        else{  
  
          echo " <a href=?page=$Previous_page>prev</a>";  
  
          echo "next";  
  
        }  
  
echo "</center></body></html>";  
  
?>  
