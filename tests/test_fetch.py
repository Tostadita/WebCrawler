#############################################################
################### WORK IN PROGRESS ########################
#############################################################

import unittest
import requests
import pytest
import main
from unittest import mock
import json

class TestCrawler(unittest.TestCase):

    def test_successful_connection(self):
        url = 'https://news.ycombinator.com/'

        # Mocking the response
        with mock.patch(target=requests.get(url), new_callable=self.get_html()) as mock_get:
            mock_response = mock.Mock()

            #main.main(url)

            mock_get.return_value = mock_response

            assert 0 == 0

    # def test_failed_connection(self):
    #     url = "https://nonexistentwebsite.com"
    #     response = requests.get(url)
    #     assert response.status_code >= 400

    def get_html(self):
        return """
        <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <table>
                        <tr class=".athing">
                            <td class="title">Rank 1</td>
                            <td class="votelinks"></td>
                            <td class="title">
                                <span href="http://www.link1.com">
                                    <a>
                                        First Title
                                    </a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score">1 point</span>
                                    <span>1 comment</span>
                                </span>
                            </td>
                        </tr>
                        <tr class=".athing">
                            <td class="title">Rank 2</td>
                            <td class="votelinks"></td>
                            <td class="title">
                                <span href="http://www.link2.com">
                                    <a>
                                        Second Title
                                    </a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score">2 points</span><
                                    <span>2 comments</span>
                                </span>
                            </td>
                        </tr>
                        <tr class=".athing">
                            <td class="title">Rank 3</td>
                            <td class="votelinks"></td>
                            <td class="title">
                                <span href="http://www.link3.com">
                                    <a>
                                        Third Title
                                    </a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                            </td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score">random</span><
                                    <span>discuss</span>
                                </span>
                            </td>
                        </tr>
                    </table>
                </body>
            </html>
            """
