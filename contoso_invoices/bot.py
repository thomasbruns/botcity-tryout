from botcity.core import DesktopBot
import pandas as pd
import os

current_dir, _DUMMY = os.path.split(os.path.abspath(__file__))

new_invoices_path = os.path.join(current_dir, 'Contoso+Coffee+Shop+Invoices.xlsx')

def not_found(label):

    print(f"Element not found: {label}")


def open_contoso_invoices(bot):

    contoso_invoices_path = "C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe"
    bot.execute(contoso_invoices_path)
    bot.wait(2000)
    bot.maximize_window()


def read_new_invoices(invoices_path=new_invoices_path):

    invoices = pd.read_excel(invoices_path)

    return invoices


def go_to_invoices(bot):

    if not bot.find( "invoices", matching=0.97, waiting_time=10000):
        not_found("invoices")
    bot.click()


def add_new_entry(bot):

    if not bot.find( "new_entry", matching=0.97, waiting_time=10000):
        not_found("new_entry")
    bot.click()


def select_status(bot, invoice_status):

    if not bot.find( "status", matching=0.97, waiting_time=10000):
        not_found("status")
    bot.click_relative(88, 15)


    if invoice_status == 'Uninvoiced':
        if not bot.find( "status_uninvoiced", matching=0.97, waiting_time=10000):
            not_found("status_uninvoiced")
        bot.click_relative(91, 43)
        
    elif invoice_status == 'Invoiced':
        if not bot.find( "status_invoiced", matching=0.97, waiting_time=10000):
            not_found("status_invoiced")
        bot.click_relative(87, 62)
        
    elif invoice_status == 'Paid':
        if not bot.find( "status_paid", matching=0.97, waiting_time=10000):
            not_found("status_paid")
        bot.click_relative(77, 87)


def register_invoice(bot, invoice):

    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(87, 13)

    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    bot.paste(str(invoice['Date']))

    # go to account
    bot.tab()
    bot.paste(invoice['Account Name'])

    # go to contact
    bot.tab()
    bot.paste(invoice['Contact Email'])
    
    # go to amount
    bot.tab()
    bot.paste(invoice['Amount'])

    select_status(bot, invoice['Status'])


def save_changes(bot):
    pass


def main():

    bot = DesktopBot()

    open_contoso_invoices(bot)

    new_invoices  = read_new_invoices()

    go_to_invoices(bot)

    for i, row in new_invoices.iterrows():
        add_new_entry(bot)
        register_invoice(bot, row)

    save_changes(bot)

if __name__ == '__main__':
    main()

