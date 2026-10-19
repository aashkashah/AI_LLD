
Requirements 
    core requirements
        create a group
        add member/user to a group
        add expense to a group
        settle expense
    out of scope
        various split types
        various settle options (payment is an external entity that always succeeds)
    
Entites
    group (resource?)
    user
    expense (transaction?)

classes 
    operator / service:
        splitwiseOperator

    class / data models
        user (1:N) -> groups 
        group (1:N) -> users
        group has multiple expenses

    enums
        expense_status: settled, unsettled



    
    