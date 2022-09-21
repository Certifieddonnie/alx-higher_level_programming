#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - function in C that inserts a number into a sorted singly linked list.
 * @head: linked list
 * @number: integer
 * Return: the address of the new node, or NULL if it failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *finder, *new_node;

	finder = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	while (number > finder->n)
	{
		finder = finder->next;
		if (!finder)
		{
			free(new_node);
			return (NULL);
		}
	}
	new_node->next = finder->next;
	finder->next = new_node;
	return (new_node);
}
