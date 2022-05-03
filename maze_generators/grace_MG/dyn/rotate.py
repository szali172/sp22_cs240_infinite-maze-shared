## Rotates a maze to the right once
def rotate_maze(geom):
  
  # Call helper to rearrange the blocks
  rearranged = rearrange(geom)
  
  r_geom = [] # Output 2D array
  
  for cells in rearranged:
    row = ''
    for i in range(0, len(cells)):
      
      # Reference variable in which converts hex to decimal
      cell = int(cells[i], 16)
      
      # 0 and 15 remain unchanged when rotated
      if cell == 0:
        cell = 0
        
      elif cell == 15:
        cell = 15
      
      # Even values have a simple pattern
      elif cell % 2 == 0:
        cell = int(cell / 2)
      
      # Odd values which have a pattern but isn't simple
      else:
        if cell == 1:
          cell = 8
        elif cell == 3:
          cell = 9
        elif cell == 5:
          cell = 10
        elif cell == 7:
          cell = 11
        elif cell == 9:
          cell = 12
        elif cell == 11:
          cell = 13
        elif cell == 13:
          cell = 14
          
      row = row + hex(cell).split('x')[-1]
      
    r_geom.append(row)
    
  return r_geom


## Helper for rotate_maze()
## Rearranges the pieces so that the rotate_maze() properly rotates each piece
def rearrange(geom):
  
  rearranged = [] # Output 2D array
  
  # First column becomes first row in rotated maze
  for i in range(0, len(geom[0])):
    new_row = ''
    
    for j in range((len(geom) - 1), -1, -1):
      new_row = new_row + geom[j][i]
      
    rearranged.append(new_row)
  
  return rearranged