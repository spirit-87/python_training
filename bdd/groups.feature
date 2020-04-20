Scenario Outline: Add new group
    # предусловия
    Given a group list
    Given a group with <name>, <header> and <footer>
    # действия
    When I add the group to the list
    # результат
    Then the new group list is equal to the old list with added group

    Examples:
    | name   | header  | footer   |
    | name 1 | header 1 | footer 1 |
    | name 2 | header 2 | footer 2 |

Scenario: Delete a group
    Given a non-empty group list
    Given a random group from the list
    When I delete the group from the list
    Then new list is equal to the old list without the deleted group

Scenario Outline: Modify a group
    Given a non-empty group list
    Given a random group from the list
    Given a group with <name_mod>, <header_mod> and <footer_mod>
    When I modify the group from the list
    Then new list is equal to the old list with the modified group

    Examples:
    | name_mod | header_mod | footer_mod |
    | name mod | header mod | footer mod |