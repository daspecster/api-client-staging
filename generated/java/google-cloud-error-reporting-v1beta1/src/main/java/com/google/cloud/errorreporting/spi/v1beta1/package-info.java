/*
 * Copyright 2016, Google Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * A client to Stackdriver Error Reporting API.
 *
 * <p>The interfaces provided are listed below, along with usage samples.
 *
 * <p>======================= ErrorGroupServiceClient =======================
 *
 * <p>Service Description: Service for retrieving and updating individual error groups.
 *
 * <p>Sample for ErrorGroupServiceClient:
 *
 * <pre>
 * <code>
 * try (ErrorGroupServiceClient errorGroupServiceClient = ErrorGroupServiceClient.create()) {
 *   String formattedGroupName = ErrorGroupServiceClient.formatGroupName("[PROJECT]", "[GROUP]");
 *   ErrorGroup response = errorGroupServiceClient.getGroup(formattedGroupName);
 * }
 * </code>
 * </pre>
 *
 * ======================= ErrorStatsServiceClient =======================
 *
 * <p>Service Description: An API for retrieving and managing error statistics as well as data for
 * individual events.
 *
 * <p>Sample for ErrorStatsServiceClient:
 *
 * <pre>
 * <code>
 * try (ErrorStatsServiceClient errorStatsServiceClient = ErrorStatsServiceClient.create()) {
 *   String formattedProjectName = ErrorStatsServiceClient.formatProjectName("[PROJECT]");
 *   DeleteEventsResponse response = errorStatsServiceClient.deleteEvents(formattedProjectName);
 * }
 * </code>
 * </pre>
 *
 * ========================= ReportErrorsServiceClient =========================
 *
 * <p>Service Description: An API for reporting error events.
 *
 * <p>Sample for ReportErrorsServiceClient:
 *
 * <pre>
 * <code>
 * try (ReportErrorsServiceClient reportErrorsServiceClient = ReportErrorsServiceClient.create()) {
 *   String formattedProjectName = ReportErrorsServiceClient.formatProjectName("[PROJECT]");
 *   ReportedErrorEvent event = ReportedErrorEvent.newBuilder().build();
 *   ReportErrorEventResponse response = reportErrorsServiceClient.reportErrorEvent(formattedProjectName, event);
 * }
 * </code>
 * </pre>
 */
package com.google.cloud.errorreporting.spi.v1beta1;
