#include "lists.h"

/**
 * check_cycle - A Function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: Linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *nextptr;

	ptr = list;
	nextptr = list;

	while (list != NULL && ptr != NULL && ptr->next != NULL)
	{
		list = list->next;
		ptr = ptr->next->next;

		if (list == ptr)
		{
			list = nextptr;
			nextptr = ptr;
			while(1)
			{
				ptr = nextptr;
				while (ptr->next != list && ptr->next != nextptr)
				{
					ptr = ptr->next;
				}
				if (ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);

}
