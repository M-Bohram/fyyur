from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL

class ShowForm(FlaskForm):
    artist_id = StringField(
        'Artist ID',
        render_kw={'class':'form-control'}
    )
    venue_id = StringField(
        'Venue ID',
        render_kw={'class':'form-control'}
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today(),
        render_kw={'class':'form-control', 'placeholder': 'YYYY-MM-DD HH:MM'}
    )

class VenueForm(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired()],
        render_kw={'class':'form-control'}
    )
    city = StringField(
        'City', validators=[DataRequired()],
        render_kw={'class':'form-control','placeholder':'City'}
    )
    state = SelectField(
        'State', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ],
        render_kw={'class':'form-control','placeholder':'State'}
    )
    address = StringField(
        'Address', validators=[DataRequired()],
        render_kw={'class':'form-control'}
    )
    phone = StringField(
        'Phone',
        render_kw={'class':'form-control','placeholder':'xxxx-xxx-xxxx'}
    )
    image_link = StringField(
        'Image Link',
        render_kw={'class':'form-control','placeholder':'https://image_url'}
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'Genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ],
        render_kw={'class':'form-control'}
    )
    facebook_link = StringField(
        'Facebook_link', validators=[URL()],
        render_kw={'class':'form-control','placeholder':'https://facebook.com/venus_page'}
    )

class ArtistForm(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired()],
        render_kw={'class':'form-control'}
    )
    city = StringField(
        'City', validators=[DataRequired()],
        render_kw={'class':'form-control'}
    )
    state = SelectField(
        'State', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ],
        render_kw={'class':'form-control'}
    )
    phone = StringField(
        # TODO implement validation logic for state
        'Phone',
        render_kw={'class':'form-control','placeholder':'xxxx-xxx-xxxx'}
    )
    image_link = StringField(
        'Image Link',
        render_kw={'class':'form-control','placeholder':'https://image_url'}
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'Genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ],
        render_kw={'class':'form-control'}
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'Facebook Link', validators=[URL()],
        render_kw={'class':'form-control','placeholder':'https://facebook.com/venus_page'}
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORMchristopher nolan movies
