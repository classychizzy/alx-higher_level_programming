#include "lists.h"
#include <stdlib.h>
#include <unistd.h>
/**
* insert_node- inserts a number in an ordered link list
* @head: double pointer to the linked list
* @number: number to be added to the new node
* Return: address to the new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *new = NULL;
listint_t *temp = NULL;
new = malloc(sizeof(listint_t));

if (!head)
	return (NULL);
new->n = number;
new->next = NULL;

if (!*head || (*head)->n > number)
{
	new->next = *head;
	return (*head = new);
}
else
{
	while (current && current->n < number)
	{
		temp->next = new;
		current = current->next;
	}
	temp->next = new;
	new->next = current;
}

return (new);
}
