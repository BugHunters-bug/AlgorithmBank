#include<stdio.h>
int main()
{
  int n,v,i;
  int a[n];
  printf("Enter the number of elements of array\n");
  scanf("%d",&n);
  printf("Enter the array values\n");//taking the array elements by using a for loop
  for (i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("Enter the value to be searched:");
  scanf("%d",&v); // value to be searched
  for (i=0;i<n;i++)
  {
    if(a[i]==v)
    {
      printf("Position of %d is %d",v,i);
      break;//breaks out of the loop
    }
  }
  return 0;
}
