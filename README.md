// C++ Program to Implement Queue using Linked List
 
#include<iostream.h>

#include<stdio.h>

#include<conio.h>

using namespace std;

struct node
{
    int da;
    node *nex;
}*front = NULL,*rear = NULL,*p = NULL,*np = NULL;
void push(int y)
{
    np = new node;
    np->da = y;
    np->nex = NULL;
    if(front == NULL)
    {
        front = rear = np;
        rear->nex = NULL;
    }
    else
    {
        rear->nex = np;
        rear = np;
        rear->nex = NULL;
    }
}
int remove()
{
    int y;
    if(front == NULL)
    {
        cout<<"empty queue\n";
    }
    else
    {
        p = front;
        y = p->da;
        front = front->nex;
        delete(p);
        return(y);
    }
}
int main()
{
    int num,c = 0,y;
    cout<<"Enter the number of values to be pushed into queue\n";
    cin>>num;
    while (c < num)
    {
	cout<<"Enter the value to be entered into queue\n";
	cin>>y;
        push(y);
        c++;
     }
     cout<<"\n\nRemoved Values\n\n";
     while(true)
     {
        if (front != NULL)
            cout<<remove()<<endl;
        else
            break;
     }
     getch();
     return 0;
}


