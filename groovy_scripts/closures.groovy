// block of code that can 
//     take parameters
//     refer variables
//     return values
//     can be passed as parameter in a method


Myclosure = {
    println "Hello"
}

Myclosure.call()

Myclosure1 = { name ->
    println "Hello $name"
}

Myclosure1.call("Madhu")


Myclosure2 = { fname, lname ->
    println "Hello $fname $lname"
}

Myclosure2.call("Madhu", "Sudhan")

str = "Hello"
Myclosure3 = {fname, lname ->
    println "$str $fname $lname"
}

Myclosure3.call("Madhu", "Sudhan")


def Mymethod(clos) {
    clos.call("Madhu")
}

Mymethod(Myclosure1)



Myclosure4 = {
    a,b,c ->
    return (a+b+c)
}

res = Myclosure4.call(10,20,30)
println res



list1 = [10,20,30]

println list1.each {
    it
}


mymap = [
    "Name" : "Madhu",
    "Age" : 25
]

println mymap.each { it }



mylist = [1,2,3,4,5]

println mylist.find {
    item ->
    item == 3
}

println mylist.findAll {
    item ->
    item > 3
}

println mylist.any{
    item ->
    item > 3
}

println mylist.every{
    item ->
    item > 3
}

println mylist.collect{
    item ->
    item*2
}