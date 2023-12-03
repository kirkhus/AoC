<?php

$stacks_single= array(
      1 => array("W", "B", "D", "N", "C", "F", "J"),
      2 => array("P", "Z", "V", "Q", "L", "S", "T"),
      3 => array("P", "Z", "B", "G", "J", "T"),
      4 => array("D", "T", "L", "J", "Z", "B", "H", "C"),
      5 => array("G", "V", "B", "J", "S"),
      6 => array("P", "S", "Q"),
      7 => array("B", "V", "D", "F", "L", "M", "P", "N"),
      8 => array("P", "S", "M", "F", "B", "D", "L", "R"),
      9 => array("V", "D", "T", "R")
);

$stacks_multiple = $stacks_single;

function move_crates_single($number, $from, $to) {
      global $stacks_single;
      $source = $stacks_single[$from];
      $target = $stacks_single[$to];  
      for ($x = 0; $x < $number; $x++) {
            $element = array_pop($source);
            $target[] = $element;
      }

      $stacks_single[$from] = $source;
      $stacks_single[$to] = $target;
}

function move_crates_multiple($number, $from, $to) {
      global $stacks_multiple;
      $source = $stacks_multiple[$from];
      $target = $stacks_multiple[$to];  

      $stacks_multiple[$to] = array_merge($stacks_multiple[$to], array_slice($source, count($source) - $number, $number));

      for ($x = 0; $x < $number; $x++) {
            $element = array_pop($source);
      }

      $stacks_multiple[$from] = $source;
}

//move 3 from 1 to 3
$pattern = "/move (\d+) from (\d+) to (\d+)/";
$lines = file("input");
 
foreach($lines as $line) {
      preg_match($pattern, $line, $matches);
      $number = $matches[1];
      $from = $matches[2];
      $to = $matches[3];

      move_crates_single($number, $from, $to);
      move_crates_multiple($number, $from, $to);
}


$single = "";
foreach ($stacks_single as $stack) {
      $single .= end($stack);
}

$multiple = "";
foreach ($stacks_multiple as $stack) {
      $multiple .= end($stack);
}

print("Part 1: " . $single . "\n");
print("Part 2: " . $multiple . "\n");

?>