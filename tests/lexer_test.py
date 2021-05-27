from typing import List
from unittest import TestCase
from typing import List
from lpp.token import (
    Token,
    TokenType
)
from lpp.lexer import Lexer


class LexerTest(TestCase):

    def validate_tes(self, source: str, expected_tokens: List[Token]) -> None:
        lexer: Lexer = Lexer(source)

        token: List[Token] = []
        for i in range(len(expected_tokens)):
            token.append(lexer.next_token())

        self.assertEquals(token, expected_tokens)

    def test_illegal(self) -> None:
        source: str = '¡¿@'

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@')
        ]

        self.validate_tes(source, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+'

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
        ]

        self.validate_tes(source, expected_tokens)

    def test_eof(self) -> None:
        source: str = '+'

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]

        self.validate_tes(source, expected_tokens)

    def test_delimiters(self) -> None:
        source = '(){},;'

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.validate_tes(source, expected_tokens)

    def test_assignment(self) -> None:
        source = 'variable cinco = 5;'

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.validate_tes(source, expected_tokens)

    def test_function_declaration(self) -> None:
        source = '''
            variable suma = procedimiento(x, y) {
                x + y;
            };
        '''

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.FUNCTION, 'procedimiento'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.validate_tes(source, expected_tokens)

    def test_function_call(self) -> None:
        source: str = """
            variable resultado = suma(dos, tres);
        """

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'resultado'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.validate_tes(source, expected_tokens)

    def test_control_statement(self) -> None:
        source: str = '''
            si (5 < 10) {
                regresa verdadero;
            } si_no {
                regresa falso;
            }
        '''

        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'si'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'regresa'),
            Token(TokenType.TRUE, 'verdadero'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'si_no'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'regresa'),
            Token(TokenType.FALSE, 'falso'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
        ]
        self.validate_tes(source,expected_tokens)
