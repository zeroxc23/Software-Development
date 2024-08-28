// Aqui en esta carpeta veremos sobre el lenguaje de programación java y 
//en este archivo en especifico los conceptos basicos 

//Comentario de una sola linea

/*
Comentario 
para 
diferentes 
lineas 
 */

package Java;
public class Conceptos_Basicos {
    public static void main(String[] args) {
        System.out.println("Hello World"); // En esta linea es la sintaxis para imprimir mensajes
        System.out.println(250); // que como en otros lenguajes acepta diferentes tipos de datos
        System.out.println(2*5);// tipo string, int hasta calucos matematicos etc
       
    /*Creación de variables */
    /*Nota: Se peude especificar o no el tipo de variable */
    /*String */
        String name="Jose";
        System.out.println(name);
     /*Asignar un nuevo valor aplica con los demas */
        String animal="Perro";
        animal="Lobo";
        System.out.println(animal);
    /*Int o entero */
        int Num=15;
        System.out.println(Num);
    /*Float */
        float floatn= 3.99f;
        System.out.println(floatn);
    /*Char */
        char letra='A';
        System.out.println(letra);
    /*Boolean */
        boolean verdadero=true;
        System.out.println(verdadero);

    /*Ahora veremos variables con la palabra clave final */
    /*Nota: Una vez que se le asigna un valor a una variable con la palabra clave
    final, no se puede cambiar */
    final int edad=20;
    System.out.println(edad);
    
    
       
}
}

