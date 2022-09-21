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
	listint_t *pointer, *new_node, *prev;

	new_node = malloc(sizeof(listint_t));
	prev = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	if (!prev)
		return (NULL);

	if (!head)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	new_node->n = number;
	pointer = *head;
	prev = *head;

	if (head)
	{
		while (number > prev->next->n)
		{
			prev = prev->next;
			pointer = pointer->next;

			if (!pointer)
			{
				free(prev);
				free(new_node);
				return (NULL);
			}
		}
		prev = prev->next;
	}
	new_node->next = prev;
	pointer->next = new_node;
	return (new_node);
}
