import datetime

# AppleScript

notes_created_date_command = "osascript -e 'tell application \"Notes\"' \
                            -e 'get get the creation date of notes of the folder \"God witnesses\"' \
                            -e 'end tell'"


# MySQl数据库登录信息

host = "localhost"
username = "root"
password = "password"
database = "God_Witnesses"

# 向database里创建列表信息

table_name = "The_Love_Between_Iris_and_Joshua"

love_sql = "CREATE TABLE IF NOT EXISTS `%s`( \
        `SEQUENCE` INT UNSIGNED AUTO_INCREMENT, \
        `EXECUTING_TIME` DATE, \
        `DATETIME` VARCHAR(50) NOT NULL, \
        `LOCATION` VARCHAR(50), \
        `WEATHER` VARCHAR(30), \
        `TITLE` VARCHAR(100), \
        `BODY` VARCHAR(100), \
        `PICTURE` VARCHAR(100), \
        `OTHERS` VARCHAR(30), \
        PRIMARY KEY (`SEQUENCE`,`DATETIME`) \
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;"%table_name

