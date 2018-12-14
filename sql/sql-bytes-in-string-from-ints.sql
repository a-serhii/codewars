select
    octet_length(CAST(number1 as text)) as octnum1,
    octet_length(CAST(number2 as text)) as octnum2,
    octet_length(CAST(number3 as text)) as octnum3,
    octet_length(CAST(number4 as text)) as octnum4,
    octet_length(CAST(number5 as text)) as octnum5
from
    numbers;