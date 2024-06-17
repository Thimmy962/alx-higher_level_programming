#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *create_new_node(int n);
listint_t *reverse(listint_t *head);
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to a pointer called head
 * Return: an int.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *ptr = *head;
	listint_t *reversed = reverse(*head);
	listint_t *ptr2 = reversed;

	while (ptr != NULL && ptr2 != NULL)
	{
		if (ptr->n != ptr2->n)
		{
			free_listint(reversed);
			return (0);
		}
		ptr = ptr->next;
		ptr2 = ptr2->next;
	}
	free_listint(reversed);
	return (1);
}

/**
 * reverse - reverse a linked list
 * @head: pointer to the beginning of the head
 * Return: an int.
 */
listint_t *reverse(listint_t *head)
{
	if (head == NULL)
	{
		return (NULL);
	}

	listint_t *reversed_head = NULL;
	listint_t *current = head;

	while (current != NULL)
	{
		listint_t *new_node;

		new_node = create_new_node(current->n);
		new_node->next = reversed_head;
		reversed_head = new_node;
		current = current->next;
	}
	return (reversed_head);
}

/**
 * create_new_node - creates a new node
 * @n: the data in the node
 * Return: an int.
 */
listint_t *create_new_node(int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = n;
	new_node->next = NULL;
	return (new_node);
}
