#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - function that inserts a number into a sorted
 * linked list.
 * @head: linked list
 * @number: integer
 * Return: the address of the new node, or NULL if it failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pointer, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	if (!*head || (*head)->n > number)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	new_node->n = number;
	pointer = *head;

	while (pointer->next)
	{
		if (pointer->next->n >= number)
		{
			new_node->next = pointer->next;
			pointer->next = new_node;
			return (new_node);

		}
		pointer = pointer->next;
	}
	new_node->next = NULL;
	pointer->next = new_node;
	return (new_node);
}
