"""crear tablas client, barber, appointment

Revision ID: 060594e341e9
Revises: 10c6a4dbe5a4
Create Date: 2023-12-22 04:22:09.300122

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '060594e341e9'
down_revision = '10c6a4dbe5a4'
branch_labels = None
depends_on = None

clients_data = [{'phone': '+1-020-936-2759', 'name': 'Cynthia Peterson', 'id': 1}, {'phone': '+1-192-375-0802', 'name': 'Kyle Sparks', 'id': 2}, {'phone': '+1-187-207-7017', 'name': 'Lisa Price', 'id': 3}, {'phone': '+1-486-787-0643', 'name': 'Shelly Ruiz', 'id': 4}, {'phone': '+1-104-290-0274', 'name': 'Jonathan Nelson', 'id': 5}, {'phone': '+1-996-911-3655', 'name': 'Jasmine Grimes', 'id': 6}, {'phone': '+1-012-284-0043', 'name': 'Daniel Summers', 'id': 7}, {'phone': '+1-779-683-7893', 'name': 'Taylor Hart', 'id': 8}, {'phone': '+1-488-394-2117', 'name': 'Kathy Wade', 'id': 9}, {'phone': '+1-231-830-7029', 'name': 'Steven Wheeler', 'id': 10}, {'phone': '+1-298-187-7182', 'name': 'Abigail Martin', 'id': 11}, {'phone': '+1-849-821-5742', 'name': 'Daisy Roberson', 'id': 12}, {'phone': '+1-914-746-2129', 'name': 'Karen Williams', 'id': 13}, {'phone': '+1-868-369-5474', 'name': 'Dylan Green', 'id': 14}, {'phone': '+1-177-200-3146', 'name': 'Amanda Smith', 'id': 15}, {'phone': '+1-013-901-7803', 'name': 'Donald Johnston DDS', 'id': 16}, {'phone': '+1-693-881-2985', 'name': 'Cheryl Edwards', 'id': 17}, {'phone': '+1-167-178-0497', 'name': 'Kathleen Dixon', 'id': 18}, {'phone': '+1-636-723-3379', 'name': 'Brian Marshall', 'id': 19}, {'phone': '+1-586-834-9079', 'name': 'Robert Lee', 'id': 20}, {'phone': '+1-169-125-9125', 'name': 'Anthony Snyder', 'id': 21}, {'phone': '+1-129-905-1650', 'name': 'Michael Rodriguez', 'id': 22}, {'phone': '+1-095-485-2315', 'name': 'Michael Adams', 'id': 23}, {'phone': '+1-806-654-9640', 'name': 'Melissa Arroyo', 'id': 24}, {'phone': '+1-772-215-4486', 'name': 'Danielle Barrett', 'id': 25},
                {'phone': '+1-773-014-4099', 'name': 'Nancy Moore', 'id': 26}, {'phone': '+1-381-632-0080', 'name': 'Tina Norton', 'id': 27}, {'phone': '+1-888-346-0680', 'name': 'Christy Rose', 'id': 28}, {'phone': '+1-327-613-7274', 'name': 'Hailey Diaz', 'id': 29}, {'phone': '+1-862-338-8666', 'name': 'Paul Guzman', 'id': 30}, {'phone': '+1-927-954-5194', 'name': 'Elizabeth Solomon', 'id': 31}, {'phone': '+1-827-095-0905', 'name': 'Russell Vincent', 'id': 32}, {'phone': '+1-073-421-5602', 'name': 'Ricky Rosario', 'id': 33}, {'phone': '+1-364-239-4343', 'name': 'Cheryl Martin MD', 'id': 34}, {'phone': '+1-466-216-9688', 'name': 'Sara Franco', 'id': 35}, {'phone': '+1-521-495-1177', 'name': 'Jamie Quinn', 'id': 36}, {'phone': '+1-889-334-9051', 'name': 'Rachel Ritter', 'id': 37}, {'phone': '+1-853-730-7238', 'name': 'Paul Mckinney', 'id': 38}, {'phone': '+1-225-160-0113', 'name': 'Vickie Rich', 'id': 39}, {'phone': '+1-274-160-3161', 'name': 'Kelly Sherman', 'id': 40}, {'phone': '+1-094-386-0916', 'name': 'Victoria Hughes', 'id': 41}, {'phone': '+1-277-155-0843', 'name': 'Jennifer Howard', 'id': 42}, {'phone': '+1-352-617-8916', 'name': 'James Green', 'id': 43}, {'phone': '+1-768-766-7779', 'name': 'Robert Pope', 'id': 44}, {'phone': '+1-712-002-7767', 'name': 'Michael Nelson', 'id': 45}, {'phone': '+1-954-063-0945', 'name': 'Benjamin Jones', 'id': 46}, {'phone': '+1-012-661-7096', 'name': 'Kenneth Wilson', 'id': 47}, {'phone': '+1-849-274-9401', 'name': 'Christina Stokes', 'id': 48}, {'phone': '+1-005-859-9538', 'name': 'Ruth Baker', 'id': 49}, {'phone': '+1-699-015-4878', 'name': 'Ryan Coffey', 'id': 50}]

barbers_data = [{'phone': '+1-622-743-4101', 'name': 'Danny Lopez', 'id': 1}, {'phone': '+1-000-754-5983', 'name': 'Ralph Wu', 'id': 2},
                {'phone': '+1-098-276-2008', 'name': 'William Todd', 'id': 3}, {'phone': '+1-198-318-1417', 'name': 'Mason Green', 'id': 4}]

appointments_data = [{
    'date': '12/19/2023 16:29',
    'client_id': 1,
    'barber_id': 1,
    'service': "Haircut"
}, {
    'date': '12/9/2023 18:12',
    'client_id': 2,
    'barber_id': 2,
    'service': "Hair Color"
}, {
    'date': '12/10/2023 8:53',
    'client_id': 3,
    'barber_id': 3,
    'service': "Beard Trim"
}, {
    'date': '12/19/2023 18:29',
    'client_id': 4,
    'barber_id': 2,
    'service': "Haircut"
}, {
    'date': '12/17/2023 4:59',
    'client_id': 5,
    'barber_id': 3,
    'service': "Facial"
}, {
    'date': '12/13/2023 10:50',
    'client_id': 6,
    'barber_id': 3,
    'service': "Shave"
}, {
    'date': '12/20/2023 4:17',
    'client_id': 7,
    'barber_id': 4,
    'service': "Haircut"
}, {
    'date': '12/12/2023 2:00',
    'client_id': 8,
    'barber_id': 3,
    'service': "Hair Color"
}, {
    'date': '12/20/2023 13:16',
    'client_id': 9,
    'barber_id': 3,
    'service': "Haircut"
}, {
    'date': '12/7/2023 22:45',
    'client_id': 10,
    'barber_id': 2,
    'service': "Beard Trim"
}, {
    'date': '12/17/2023 16:46',
    'client_id': 11,
    'barber_id': 4,
    'service': "Hair Color"
}, {
    'date': '12/15/2023 22:28',
    'client_id': 12,
    'barber_id': 1,
    'service': "Beard Trim"
}, {
    'date': '12/20/2023 3:38',
    'client_id': 13,
    'barber_id': 4,
    'service': "Facial"
}, {
    'date': '12/18/2023 0:50',
    'client_id': 14,
    'barber_id': 4,
    'service': "Shave"
}, {
    'date': '12/8/2023 4:25',
    'client_id': 15,
    'barber_id': 3,
    'service': "Hair Color"
}, {
    'date': '12/19/2023 6:14',
    'client_id': 16,
    'barber_id': 4,
    'service': "Shave"
}, {
    'date': '12/18/2023 17:24',
    'client_id': 17,
    'barber_id': 1,
    'service': "Facial"
}, {
    'date': '12/7/2023 21:00',
    'client_id': 18,
    'barber_id': 3,
    'service': "Beard Trim"
}, {
    'date': '12/13/2023 13:01',
    'client_id': 19,
    'barber_id': 1,
    'service': "Hair Color"
}, {
    'date': '12/14/2023 12:29',
    'client_id': 20,
    'barber_id': 2,
    'service': "Haircut"
}, {
    'date': '12/9/2023 22:10',
    'client_id': 21,
    'barber_id': 1,
    'service': "Shave"
}, {
    'date': '12/10/2023 17:29',
    'client_id': 22,
    'barber_id': 3,
    'service': "Shave"
}, {
    'date': '12/7/2023 22:49',
    'client_id': 23,
    'barber_id': 1,
    'service': "Haircut"
}, {
    'date': '12/18/2023 19:06',
    'client_id': 24,
    'barber_id': 4,
    'service': "Shave"
}, {
    'date': '12/13/2023 22:14',
    'client_id': 25,
    'barber_id': 4,
    'service': "Hair Color"
}, {
    'date': '12/18/2023 4:29',
    'client_id': 26,
    'barber_id': 2,
    'service': "Facial"
}, {
    'date': '12/10/2023 21:29',
    'client_id': 27,
    'barber_id': 1,
    'service': "Facial"
}, {
    'date': '12/12/2023 1:35',
    'client_id': 28,
    'barber_id': 2,
    'service': "Facial"
}, {
    'date': '12/19/2023 14:48',
    'client_id': 29,
    'barber_id': 4,
    'service': "Facial"
}, {
    'date': '12/10/2023 5:26',
    'client_id': 30,
    'barber_id': 2,
    'service': "Beard Trim"
}, {
    'date': '12/19/2023 19:15',
    'client_id': 31,
    'barber_id': 2,
    'service': "Haircut"
}, {
    'date': '12/11/2023 12:14',
    'client_id': 32,
    'barber_id': 1,
    'service': "Hair Color"
}, {
    'date': '12/10/2023 10:05',
    'client_id': 33,
    'barber_id': 2,
    'service': "Beard Trim"
}, {
    'date': '12/19/2023 17:08',
    'client_id': 34,
    'barber_id': 4,
    'service': "Shave"
}, {
    'date': '12/9/2023 16:11',
    'client_id': 35,
    'barber_id': 3,
    'service': "Shave"
}, {
    'date': '12/19/2023 1:30',
    'client_id': 36,
    'barber_id': 4,
    'service': "Shave"
}, {
    'date': '12/13/2023 11:34',
    'client_id': 37,
    'barber_id': 3,
    'service': "Haircut"
}, {
    'date': '12/12/2023 20:07',
    'client_id': 38,
    'barber_id': 1,
    'service': "Beard Trim"
}, {
    'date': '12/19/2023 7:15',
    'client_id': 39,
    'barber_id': 1,
    'service': "Hair Color"
}, {
    'date': '12/11/2023 10:24',
    'client_id': 40,
    'barber_id': 1,
    'service': "Hair Color"
}, {
    'date': '12/9/2023 16:58',
    'client_id': 41,
    'barber_id': 3,
    'service': "Facial"
}, {
    'date': '12/8/2023 8:42',
    'client_id': 42,
    'barber_id': 3,
    'service': "Beard Trim"
}, {
    'date': '12/17/2023 19:51',
    'client_id': 43,
    'barber_id': 3,
    'service': "Hair Color"
}, {
    'date': '12/14/2023 9:08',
    'client_id': 44,
    'barber_id': 3,
    'service': "Beard Trim"
}, {
    'date': '12/10/2023 23:18',
    'client_id': 45,
    'barber_id': 1,
    'service': "Facial"
}, {
    'date': '12/13/2023 16:40',
    'client_id': 46,
    'barber_id': 2,
    'service': "Beard Trim"
}, {
    'date': '12/17/2023 9:44',
    'client_id': 47,
    'barber_id': 4,
    'service': "Haircut"
}, {
    'date': '12/12/2023 21:53',
    'client_id': 48,
    'barber_id': 2,
    'service': "Hair Color"
}, {
    'date': '12/7/2023 22:02',
    'client_id': 49,
    'barber_id': 4,
    'service': "Hair Color"
}, {
    'date': '12/9/2023 16:30',
    'client_id': 50,
    'barber_id': 4,
    'service': "Shave"
}]

for appointment in appointments_data:
    appointment['date'] = datetime.strptime(
        appointment['date'], '%m/%d/%Y %H:%M')


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barber',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('phone', sa.String(length=20), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('client',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('phone', sa.String(length=20), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('appointment',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.Column('service', sa.String(length=50), nullable=False),
                    sa.Column('client_id', sa.Integer(), nullable=False),
                    sa.Column('barber_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['barber_id'], ['barber.id'], ),
                    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    barber_table = sa.Table('barber', sa.MetaData(),
                            autoload_with=op.get_bind())

    op.bulk_insert(barber_table, barbers_data)

    client_table = sa.Table('client', sa.MetaData(),
                            autoload_with=op.get_bind())

    op.bulk_insert(client_table, clients_data)

    appointment_table = sa.Table('appointment', sa.MetaData(),
                                 autoload_with=op.get_bind())

    op.bulk_insert(appointment_table, appointments_data)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    op.drop_table('client')
    op.drop_table('barber')
    # ### end Alembic commands ###
