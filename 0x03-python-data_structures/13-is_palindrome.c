#include "lists.h"

/**
 * is_palindrome - check for palindrome linkedlist
 * @head: linkedlist
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int buf[10240], i = 0, end = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (temp)
	{
		buf[end] = temp->n;
		temp = temp->next;
		end++;
	}
	end--;

	while (i <= (end / 2))
	{
		if (buf[i] != buf[end - i])
			return (0);
		i++;
	}
	return (1);
}
