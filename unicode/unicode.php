<?php
/**
 *  Demo
 * 
 * @author wang chong(wangchong1985@gmail.com)
 * @link http://www.wangchong.org
 * @version 1.0.0 (2011-04-15)
 * @package php-Unicode
 */

include 'unicode.class.php';



$str = "";

$convert = new Unicode();

//convert to Unicode
//var_dump($str = $convert->str_to_unicode($str, 'UTF-8'));

//convert to UTF-8
var_dump($str = $convert->str_from_unicode($str, 'UTF-8'));
