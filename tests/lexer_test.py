from typing import List
from unittest import TestCase
from typing import List
from lpp.token import (
    Token,
    TokenType
)
from lpp.lexer import Lexer


class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@')
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+'
        lexer: Lexer = Lexer(source)

        token: List[Token] = []
        for i in range(len(source)):
            token.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
        ]

        self.assertEquals(token, expected_tokens)

    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        token: List[Token] = []
        for i in range(len(source) + 1):
            token.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]

        self.assertEquals(token, expected_tokens)

    def test_delimiters(self) -> None:
        source = '(){},;'
        lexer: Lexer = Lexer(source)

        token: List[Token] = []
        for i in range(len(source)):
            token.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.RPAREN, '('),
            Token(TokenType.LPAREN, ')'),
            Token(TokenType.RBRACE, '{'),
            Token(TokenType.LBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEquals(token, expected_tokens)

    def test_assignment(self) -> None:
        source = 'variable cinco = 5;'
        lexer: Lexer = Lexer(source)

        token: List[Token] = []
        for i in range(5):
            token.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEquals(token, expected_tokens)
