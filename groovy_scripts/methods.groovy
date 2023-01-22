def printHello(){
    println "Hello"
}

def sum(int a=10,int b=20){
    println "sum is " + (a+b)
}
printHello()


sum()
sum(20,67)
sum(6)

def sub(int a,int b){
    c = a-b
    return c
}

res = sub(11,9)
println "res is $res"