from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

try:
    with Booking() as bot: # teardown=True if want to close browser everytime
        bot.land_first_page()
        # print("Exiting...")
        bot.change_currency(currency="USD")
        bot.select_place_to_go("New York")
        bot.select_date(check_in_date='2022-05-16', check_out_date='2022-05-23')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()

except Exception as e:
    if 'IN PATH' in str(e):
        print("There is a problem running this program from command line interface")
    else:
        raise