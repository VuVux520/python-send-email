import unittest

from send_emails import send_email

import os

import csv

class TestSendEmail(unittest.TestCase):

  def test_send_email(self):
    list = os.listdir('sentEmails')
    expected = len(list) + 2
    send_email('customers.csv', 'email_template.json', 'error.csv')
    actual = len(os.listdir('sentEmails'))
    self.assertEqual(actual, expected)
  
  def test_no_email(self):
    file = open('error_test.csv', 'r')
    reader = csv.reader(file)
    expected= len(list(reader)) + 1
    send_email('customers.csv', 'email_template.json', 'error_test.csv')
    file = open('error_test.csv', 'r')
    reader = csv.reader(file)
    actual = len(list(reader))
    self.assertEqual(actual, expected)

  def test_empty_customer(self):
    with self.assertRaises(Exception) as exception_context:
      send_email('empty_customer.csv', 'email_template.json', 'error.csv')
    self.assertEqual(
      str(exception_context.exception),
      "No customers found"
    )
    
  def test_no_email_save_data(self):
    file = open('error.csv', 'r')
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      self.assertEqual(row[0], 'Mr')
      self.assertEqual(row[1], 'James')
      self.assertEqual(row[2], 'Bond')

if __name__ == '__main__':
    unittest.main(verbosity=2)
