FROM mhart/alpine-node:11 AS builder

RUN mkdir React_dashboard
COPY ./React_dashboard ./React_dashboard

WORKDIR /React_dashboard

RUN yarn run build


FROM mhart/alpine-node
RUN yarn global add serve

WORKDIR /React_dashboard

COPY --from=builder /React_dashboard/build .
CMD ["serve", "-p", "3000", "-s", "."]