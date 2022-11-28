using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Triger : MonoBehaviour
{
    public Perceptron perceptron;
    public GameObject sphere1;
    public GameObject sphere2;
    public void OnTriggerEnter(Collider other)
    {
        int sphere1L = 0;
        int sphere2L = 0;
        if (sphere1.GetComponent<Renderer>().material.color == Color.blue)
        {
            sphere1L = 1;
        }
        if (sphere2.GetComponent<Renderer>().material.color == Color.blue)
        {
            sphere2L = 1;
        }


        var result = perceptron.CalcOutput(sphere1L, sphere2L);

        if (result == 0)
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.red;
            this.gameObject.GetComponent<Renderer>().material.color = Color.red;
        }
        else
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.blue;
            this.gameObject.GetComponent<Renderer>().material.color = Color.blue;
        }
        return;
    }
}
