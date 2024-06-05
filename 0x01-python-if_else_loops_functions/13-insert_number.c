#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  * insert_node - insert a node into a sorted linked list
  * @head: a pointer to the head which is also a pointer
  * @number: the data in the new node
  * Return: the address of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	ptr = *head;
	while (ptr != NULL && ptr->next->n < number)
	{
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
