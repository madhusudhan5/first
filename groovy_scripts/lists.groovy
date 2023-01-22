// Works similar to list in python

fruits = ["Apples","Oranges","Grapes"]

println fruits[1]
println fruits.get(2)

mylist = [1,2,3,["Hi","Helllo",3],4, "jf"]

println mylist
println mylist[3][2]
println mylist.get(3).get(2)

println mylist[1..3]
println mylist[4..2]


println mylist.contains(3)
println mylist.contains("Hi")

println mylist.size()

mylist.add(10)
println mylist

mylist<<20
println mylist

mylist.remove(2)
println mylist

mylist = mylist + [90,100]
println mylist

