#!/usr/bin/env kotlin

import java.io.File
import kotlin.math.abs

// part 1
val filePath = "input.txt"
val file = File(filePath)

fun part1(file: File) {
    var count = 0;
    for (line in file.readLines()) {
        val values = line.split(" ")
        var prev: Int? = null;
        var diff = 0;
        var direction: Int? = null;
        var isSafe = true;
        for (item in values) {
            var num = item.toInt()
            if (prev != null) {
                diff = num - prev;
                if (diff == 0 || abs(diff) > 3) { isSafe = false; break;}
                if (direction == null) {
                    direction = diff / abs(diff)
                } else {
                    if (direction != diff/abs(diff)) { isSafe = false; break;}
                }
            }
            prev = num
        }
        println(isSafe)
        if (isSafe) count++;
    }
    println("Part 1 answer: $count")

}

if (file.exists()) {
    part1(file)


} else {
    println("File not found.")
}