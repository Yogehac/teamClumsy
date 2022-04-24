import tabula

table_file = r"C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\QUOTATION NO.330.pdf"
output_csv = r"C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\QUOTATION NO.330.csv"
df = tabula.convert_into(table_file, output_csv, output_format='csv', lattice=True, stream=False, pages="all")

requestA1 = {
    'template': {
        'kattur sugar unit': {
            'Cane Carrier Chain 6" Pitch': {
                'Qty': 45,
                'dr': 45,
                'rate': 45
            }
        },
        'kattur sugar unit1': {},
        'kattur sugar unit2': {},
        'kattur sugar uni3': {}
    },
    "Replies": {
        'raj amar': {
            'Quotation': {

            },
        },
        'boomer': {
            'Quotation': {

            },
        }
    }
}
