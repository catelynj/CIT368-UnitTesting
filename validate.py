import re

class Validate:

  @staticmethod
  def zip(input):
    if re.match("^[0-9]{5}$", input):
      return True
    return False
  
  @staticmethod
  def minor(age):
    if isinstance(age, int) and 0 < age <= 17:
        return True
    return False
      
    
  
  @staticmethod 
  def email(input):
    if isinstance(input, str) and re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", input):
      return True
    return False
  
  @staticmethod
  def is_lat(number):
    if isinstance(number, (int, float)) and -90 <= number <= 90: 
      return True
    return False
  
  @staticmethod
  def is_lng(number):
    if isinstance(number, (int, float)) and number >= -180 and number <= 180: 
      return True
    return False
  
  @staticmethod
  def is_domain(input):
    if isinstance(input, str) and re.match("^[a-zA-Z0-9-]{2,253}\\.[a-zA-Z]{1}[a-zA-Z0-9]{1,}$", input):
      return True
    return False
  
  @staticmethod
  def is_url(input):
    if isinstance(input, str) and re.match("^http(s)?:\\/\\/(.*?)\\.[a-z]{2,52}\\/.*$", input):
      return True
    return False
  
  @staticmethod
  def grade(value):
    if isinstance(value, (int, float)):
        if (value < 60 and value >= 0):
          return 'F'
        if (value >= 60 and value < 70):
          return 'D'
        if (value >= 70 and value < 80):
          return 'C'
        if (value >= 80 and value < 90):
          return 'B'
        if (value >= 90 and value <= 100):
          return 'A'
    return False
      
    
  @staticmethod
  def sanitize(sql : str) -> str:
    sql = sql.upper().replace("ADMIN", "")
    sql = sql.upper().replace("OR", "")
    sql = sql.upper().replace("COLLATE", "")
    sql = sql.upper().replace("DROP", "")
    sql = sql.upper().replace("AND", "")
    sql = sql.upper().replace("UNION", "")
    sql = sql.replace("/*", "")
    sql = sql.replace("*/", "")
    sql = sql.replace("//", "")
    sql = sql.replace(";", "")
    sql = sql.replace("||", "")
    sql = sql.replace("&&", "")
    sql = sql.replace("--", "")
    sql = sql.replace("#", "")
    sql = sql.replace("=", "")
    sql = sql.replace("!=", "")
    sql = sql.replace("<>", "")

    return sql

  @staticmethod
  def strip_null(input : str) -> str:
    null_char = ["\x00", "", "\N{NULL}"]
    for char in null_char:
      input = input.replace(char, "")
    return input

  @staticmethod
  def ip(input) -> bool:
    if isinstance(input, str) and re.match("^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$", input):
          return True
    return False
  
  @staticmethod
  def mac(input) -> bool:
    if isinstance(input, str) and re.match("^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$", input.capitalize()):
      return True
    return False
  

  @staticmethod
  def md5(input) -> bool:
    if isinstance(input, str) and re.match(r"^[a-fA-F0-9]{32}$", input):
      return True
    return False