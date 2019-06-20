program MorseCoding;

function checkUserInput(userString: string): boolean;
var
  valid: boolean;
  count: integer;
begin
  valid := true;
  for count := 1 to length(userString) do
    if ((ord(userString[count]) < 65) or (ord(userString[count]) > 90)) and (userString[count] <> ' ') then
      valid := false;
  checkUserInput := valid;
end;

function getCharacterCode(character: char): string;
const
  translationArray: array [0..25] of string = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..');
begin
  if character = ' ' then
    getCharacterCode := '| '
  else
    begin
      getCharacterCode := translationArray[ord(character) - 65] + ' ';
    end;
end;

procedure main();
var
  userString, codedString: string;
  count: integer;
begin
  write('Enter a string: ');
  readln(userString);
  if checkUserInput(upcase(userString)) then
    begin
      for count := 1 to length(userString) do
        begin
          codedString := concat(codedString, getCharacterCode(upcase(userString[count])));
        end;
      writeln(codedString);
    end
  else
    writeln('Invalid input!');
end;

begin
  main();
  readln;
end.