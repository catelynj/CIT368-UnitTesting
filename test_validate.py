from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        li = ['15646', '17701', '17028', '10101', '00000']
        #HAPPY PATH
        for string in li:
            self.assertTrue(Validate.zip(string))

    def test_zip_bad(self):
        #ABUSE
        f = open("./blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))
            
    def test_age_happy(self):
        #HAPPY PATH
        for age in range(1, 18):
            self.assertTrue(Validate.minor(age))
            
        for age in range(18,119):
            self.assertFalse(Validate.minor(age))

    def test_age_bad(self):
        #ABUSE
        invalid_ages = ['eighteen', None, -1, 17.5, {}, [],'', ' ']
        for age in invalid_ages:
            self.assertFalse(Validate.minor(age))
            
    def test_email_happy(self):
        #HAPPY HAPPY HAPPY
        valid_emails = ['yomama1234@gmail.com', 'isanicelady@aol.com']
        for email in valid_emails:
            self.assertTrue(Validate.email(email))
                
    def test_email_bad(self):
        #ABUSE
        invalid_emails = ['plainaddress', '@missingusername.com', 'username@.com', 'username@com', None, '', ' ', 12345, {}, [], True, False]
        for email in invalid_emails:
            self.assertFalse(Validate.email(email))
            
    def test_is_lat_happy(self):
        #HAPPY HAPPY HAPPY
        valid_lats = [-90, 0.00, 90, 89.99,]
        for lat in valid_lats:
            self.assertTrue(Validate.is_lat(lat))

    def test_is_lat_bad(self):
        #ABUSE
        invalid_lats = [-91, 91, None, '', 'latitude', {}, []]
        for lat in invalid_lats:
            self.assertFalse(Validate.is_lat(lat))
    
    def test_is_lng_happy(self):
        #HAPPY HAPPY HAPPY
        valid_lngs = [-180, 0, 180, 179.99]
        for lng in valid_lngs:
            self.assertTrue(Validate.is_lng(lng))

    def test_is_lng_bad(self):
        #ABUSE
        invalid_lngs = [-181, 181, None, '', ' ', 'longitude', {}, []]
        for lng in invalid_lngs:
            self.assertFalse(Validate.is_lng(lng))
            
    def test_is_domain_happy(self):
        #HAPPY HAPPY HAPPY
        valid_domains = ['google.com', 'twitch.tv', 'youtube.com']
        for domain in valid_domains:
            self.assertTrue(Validate.is_domain(domain))

    def test_is_domain_bad(self):
        #ABUSE
        invalid_domains = ['totallyrealdomain', 'superlegitdomaindotcom', '.org', 'domain.', None, '', ' ', 12345, {}, [], True, False]
        for domain in invalid_domains:
            self.assertFalse(Validate.is_domain(domain))
            
    def test_is_url_happy(self):
        #HAPPY HAPPY HAPPY
        valid_urls = ['https://www.twitch.tv/', 'https://www.youtube.com/', 'https://www.google.com/']
        for url in valid_urls:
            self.assertTrue(Validate.is_url(url))
            
    def test_is_url_bad(self):
        #ABUSE
        invalid_urls = ['totallyrealurl.gov', 'http:/uber-real-url.com', 'abcd://superrealurl.gg', None, '', ' ', 12345, {}, [], True, False]
        for url in invalid_urls:
            self.assertFalse(Validate.is_url(url))
            
    def test_grade_happy(self):
        valid_grade = 100
        self.assertEqual(Validate.grade(valid_grade), 'A')
        valid_grade2 = 50
        self.assertEqual(Validate.grade(valid_grade2), 'F')

    def test_grade_bad(self):
        #ABUSE
        invalid_grades = ['A', 'B', None, '', ' ', -1, 101, {}, []]
        for grade in invalid_grades:
            self.assertFalse(Validate.grade(grade))
                
    def test_strip_null_happy(self):
        #HAPPY HAPPY HAPPY
        valid_input = 'Hello\x00, World\x00!'
        self.assertEqual(Validate.strip_null(valid_input), 'Hello, World!')
    
    def test_strip_null_bad(self):
        #ABUSE
        invalid_inputs = [None, 12345, {}, [], True, False]
        for input in invalid_inputs:
            with self.assertRaises(AttributeError):
                Validate.strip_null(input)
                
    def test_ip_happy(self):
        #HAPPY HAPPY HAPPY
        valid_ips=['195.91.183.43', '102.228.221.172', '95.129.170.253']
        for ip in valid_ips:
            self.assertTrue(Validate.ip(ip))

    def test_ip_bad(self):
        #ABUSE
        invalid_ips = ['999.999.999.999', '256.256.256.256', 'abcd', None, '', ' ', {}, [], True, False]
        for ip in invalid_ips:
            self.assertFalse(Validate.ip(ip))
            
    def test_mac_happy(self):
        #HAPPY HAPPY HAPPY
        valid_macs = ['34:89:F4:9C:91:F2', '7E:2D:6D:BC:AE:77', 'F8:44:71:55:CA:6A']
        for mac in valid_macs:
            self.assertTrue(Validate.mac(mac))

    def test_mac_bad(self):
        #ABUSE
        invalid_macs = ['00:00:00:00:00', 'invalid-mac', None, '', ' ', {}, [], True, False]
        for mac in invalid_macs:
            self.assertFalse(Validate.mac(mac))
            
    def test_md5_happy(self):
        #HAPPY HAPPY HAPPY
        valid_md5s = ['ada50c95b53827bf7fde933a7cc520a0', '4f25cb71d2d14773f50a12388b474417', 'ca3465a4cac9540b51732e32e5847c3e']
        for md5 in valid_md5s:
            self.assertTrue(Validate.md5(md5))

    def test_md5_bad(self):
        #ABUSE
        invalid_md5s = ['notamd5hash', '123', None, '', ' ', {}, [], True, False]
        for md5 in invalid_md5s:
            self.assertFalse(Validate.md5(md5))
       
if __name__ == '__main__':
    unittest.main()
