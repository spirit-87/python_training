Scenario Outline: Add new contact
    # предусловия
    Given a contact list
    Given a contact with <firstname>, <lastname> and <address>
    # действия
    When I add the contact to the list
    # результат
    Then the new contact list is equal to the old list with added contact

    Examples:
    | firstname   | lastname   | address   |
    | firstname 1 | lastname 1 | address 1 |
    | firstname 2 | lastname 2 | address 2 |

Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then new list is equal to the old list without the deleted contact

Scenario Outline: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a contact with <firstname_mod>, <lastname_mod> and <address_mod>
    When I modify the contact from the list
    Then new list is equal to the old list with the modified contact

    Examples:
    | firstname_mod | lastname_mod | address_mod |
    | firstname mod | lastname mod | address mod |