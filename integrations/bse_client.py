from tempfile import gettempdir

from bse import BSE


class BSEClient:

    def get_announcements(self):

        announcements = []

        try:

            with BSE(gettempdir()) as bse:

                result = bse.announcements(
                    page_no=1
                )

                items = result.get(
                    "Table",
                    []
                )

                for item in items:

                    analysis_text = " ".join([

                        str(
                            item.get(
                                "HEADLINE",
                                ""
                            )
                        ),

                        str(
                            item.get(
                                "NEWSSUB",
                                ""
                            )
                        ),

                        str(
                            item.get(
                                "SUBCATNAME",
                                ""
                            )
                        ),

                        str(
                            item.get(
                                "CATEGORYNAME",
                                ""
                            )
                        )
                    ])

                    announcements.append({

                        "exchange_id":
                            str(
                                item.get(
                                    "NEWSID",
                                    ""
                                )
                            ),

                        "scrip_code":
                            str(
                                item.get(
                                    "SCRIP_CD",
                                    ""
                                )
                            ),

                        "company_name":
                            str(
                                item.get(
                                    "SLONGNAME",
                                    ""
                                )
                            ),

                        "headline":
                            str(
                                item.get(
                                    "NEWSSUB",
                                    ""
                                )
                            ),

                        "analysis_text":
                            analysis_text,

                        "attachment_name":
                            str(
                                item.get(
                                    "ATTACHMENTNAME",
                                    ""
                                )
                            ),

                        "announcement_time":
                            str(
                                item.get(
                                    "DissemDT",
                                    ""
                                )
                            )
                    })

        except Exception as e:

            print(
                f"BSE Error: {e}"
            )

        return announcements