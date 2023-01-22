filepath = "data.txt"

File myfile = new File(filepath)


//Treating whole file as string
println myfile.text

//collect lines into a list
list = myfile.collect { it }
println list

//Store file content in an array
array = myfile as String[]
println array

//read file into a list of String
lines = myfile.readLines()
println lines

// Accesing file line by line using closure
myfile.eachLine { line ->
    println line
}

lineNoRange = 2..4
lineList = []
myfile.eachLine { line, lineno ->
    if (lineNoRange.contains(lineno)) {
        lineList.add(line)
    }
}
println lineList
