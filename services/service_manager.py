from datetime import datetime
import threading

import streamlit as st

from integrations.bse_client import BSEClient
from monitors.announcement_monitor import AnnouncementMonitor
from analysis.statistics_engine import StatisticsEngine

from services.service_state import service_state
from services.monitor_thread import monitor_loop
import services.thread_registry as thread_registry


class ServiceManager:


    def initialize_service(
        self,
        service_name,
        interval=60
    ):

        defaults = {

            "running": False,

            "interval": interval,

            "last_run": None,

            "records_processed": 0,

            "error_count": 0

        }

        for key, value in defaults.items():

            state_key = f"{service_name}_{key}"

            if state_key not in st.session_state:

                st.session_state[state_key] = value


    def start_service(
        self,
        service_name
    ):

        st.session_state[
            f"{service_name}_running"
        ] = True

        service_state[
            service_name
        ][
            "running"
        ] = True

        if service_name == "monitor":

            if (

                thread_registry.monitor_thread is None

                or

                not thread_registry.monitor_thread.is_alive()

            ):

                print(
                    "Starting monitor thread..."
                )

                thread_registry.monitor_thread = (

                    threading.Thread(

                        target=monitor_loop,

                        daemon=True

                    )

                )

                thread_registry.monitor_thread.start()


    def stop_service(
        self,
        service_name
    ):

        st.session_state[
            f"{service_name}_running"
        ] = False

        service_state[
            service_name
        ][
            "running"
        ] = False

        print(
            f"{service_name} stopped."
        )


    def run_now(
        self,
        service_name
    ):

        try:

            if service_name == "monitor":

                client = BSEClient()

                monitor = AnnouncementMonitor(
                    client
                )

                monitor.run()

            elif service_name == "statistics":

                stats = StatisticsEngine()

                stats.get_total_announcements()

                stats.get_event_counts()

                stats.get_average_alpha_score()

            st.session_state[
                f"{service_name}_last_run"
            ] = datetime.now().strftime(
                "%H:%M:%S"
            )

            st.session_state[
                f"{service_name}_records_processed"
            ] += 1

        except Exception as e:

            st.session_state[
                f"{service_name}_error_count"
            ] += 1

            st.error(
                str(e)
            )


    def get_info(
        self,
        service_name
    ):

        return {

            "running":

                st.session_state[
                    f"{service_name}_running"
                ],

            "interval":

                service_state[
                    service_name
                ][
                    "interval"
                ],

            "last_run":

                service_state[
                    service_name
                ][
                    "last_run"
                ],

            "records_processed":

                service_state[
                    service_name
                ][
                    "records_processed"
                ],

            "error_count":

                service_state[
                    service_name
                ][
                    "error_count"
                ]

        }