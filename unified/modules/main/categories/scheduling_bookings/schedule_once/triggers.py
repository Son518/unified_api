from unified.core.triggers import Triggers
from scheduling_bookings.schedule_once.entities.booking_canceled import BookingCanceled
from scheduling_bookings.schedule_once.entities.booking_scheduled import BookingScheduled
from scheduling_bookings.schedule_once.entities.canceled_booking_rescheduled import CanceledBookingRecheduled
from scheduling_bookings.schedule_once.entities.no_show_booking import NoShowBooking
import json


class ScheduleOnce_Triggers(Triggers):

    def booking_canceled(self, contact, payload):
        """ Triggers when a booking is canceled"""

        response = BookingCanceled(
            booking_id = payload["data"]["id"],
            creation_time = payload["data"]["creation_time"],
            starting_time = payload["data"]["starting_time"],
            event_type = payload["type"],
            subject = payload["data"]["subject"],
            status = payload["data"]["status"],
            duration_minutes = payload["data"]["duration_minutes"],
            event_description = payload["data"]["event_type"]["description"],
            virtual_or_physical_location = payload["data"]["virtual_or_physical_location"],
            canceled_rescheduled_customer = payload["data"]["name_of_customer_who_canceled_rescheduled"],
            canceled_rescheduled_user = payload["data"]["name_of_user_who_canceled_rescheduled"],
            time_zone_description = payload["data"]["booking_page"]["time_zone_description"],
            guests = payload["data"]["form_submission"]["guests"],
            booking_link = payload["data"]["booking_page"]["link"],
            cancel_reschedule_link = payload["data"]["cancel_reschedule_link"],
            mobile_phone = payload["data"]["form_submission"]["mobile_phone"],
            owner = payload["data"]["owner"]
        )
        return response.__dict__

    def booking_scheduled(self, contact, payload):
        """ Triggers when a new booking is scheduled"""
    
        response = BookingScheduled(
            booking_id = payload["data"]["id"],
            creation_time = payload["data"]["creation_time"],
            starting_time = payload["data"]["starting_time"],
            event_type = payload["type"],
            subject = payload["data"]["subject"],
            status = payload["data"]["status"],
            duration_minutes = payload["data"]["duration_minutes"],
            event_description = payload["data"]["event_type"]["description"],
            virtual_or_physical_location = payload["data"]["virtual_or_physical_location"],
            time_zone_description = payload["data"]["booking_page"]["time_zone_description"],
            guests = payload["data"]["form_submission"]["guests"],
            booking_link = payload["data"]["booking_page"]["link"],
            owner = payload["data"]["owner"]
        )
        return response.__dict__

    def canceled_booking_rescheduled(self, contact, payload):
        """ Triggers when a booking is canceled and replaced by a rescheduled booking"""
        
        response = CanceledBookingRecheduled(
            booking_id = payload["data"]["id"],
            creation_time = payload["data"]["creation_time"],
            starting_time = payload["data"]["starting_time"],
            event_type = payload["type"],
            subject = payload["data"]["subject"],
            status = payload["data"]["status"],
            duration_minutes = payload["data"]["duration_minutes"],
            event_description = payload["data"]["event_type"]["description"],
            virtual_or_physical_location = payload["data"]["virtual_or_physical_location"],
            canceled_rescheduled_customer = payload["data"]["name_of_customer_who_canceled_rescheduled"],
            canceled_rescheduled_user = payload["data"]["name_of_user_who_canceled_rescheduled"],
            time_zone_description = payload["data"]["booking_page"]["time_zone_description"],
            guests = payload["data"]["form_submission"]["guests"],
            booking_link = payload["data"]["booking_page"]["link"],
            cancel_reschedule_link = payload["data"]["cancel_reschedule_link"],
            owner = payload["data"]["owner"]
        )
        return response.__dict__
        
    def no_show_booking(self, contact, payload):
        """ Triggers when the status of a booking is changed to No-show"""
        
        response = CanceledBookingRecheduled(
            booking_id = payload["data"]["id"],
            creation_time = payload["data"]["creation_time"],
            starting_time = payload["data"]["starting_time"],
            event_type = payload["type"],
            subject = payload["data"]["subject"],
            status = payload["data"]["status"],
            duration_minutes = payload["data"]["duration_minutes"],
            event_description = payload["data"]["event_type"]["description"],
            virtual_or_physical_location = payload["data"]["virtual_or_physical_location"],
            time_zone_description = payload["data"]["booking_page"]["time_zone_description"],
            guests = payload["data"]["form_submission"]["guests"],
            booking_link = payload["data"]["booking_page"]["link"],
            cancel_reschedule_link = payload["data"]["cancel_reschedule_link"],
            owner = payload["data"]["owner"]
        )
        return response.__dict__