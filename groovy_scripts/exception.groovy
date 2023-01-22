// try-catch
// try-catch-finally
// try-finally

try{
    int i=1/0;
}
catch(ArithmeticException exp1){
    println "instance of ArithmeticException"
    println exp1.getMessage()
}
catch(Exception exp){
    println "inside excetion block"
    println exp.getMessage()
}
finally{
    println "finally"
}

println "Rest of code"