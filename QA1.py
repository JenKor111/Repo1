import time

from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser

browser.open('https://todomvc.com/examples/emberjs/#/');

browser.element('#new-todo').type('тобі').press_enter()
browser.element('#new-todo').type('привіт').press_enter()
browser.element('#new-todo').type('пока').press_enter()
browser.all('#todo-list>li').should(have.exact_texts('тобі', 'привіт', 'пока'))

browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
browser.all('#todo-list>li.completed').should(have.texts('привіт'))
browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('тобі', 'пока'))

browser.element(by.text('Completed')).click()

browser.element('#ember9').click()
browser.element('#ember8').click()

input('Enter')
browser.closer()