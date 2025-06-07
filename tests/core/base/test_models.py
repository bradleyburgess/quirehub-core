from core.base.models import BaseModel, TimestampsMixin, UuidMixin


class TestTimestampsMixin:
    def test_model_has_timestamps(self):
        class ObjectWithTimestamps(TimestampsMixin):
            class Meta:  # type: ignore
                app_label = "base"

        obj = ObjectWithTimestamps()
        for field in ("created_at", "modified_at"):
            assert hasattr(obj, field)


class TestUuidMixin:
    def test_model_has_uuid(self):
        class ObjectWithUuid(UuidMixin):
            class Meta:  # type: ignore
                app_label = "base"

        obj = ObjectWithUuid()
        assert hasattr(obj, "uuid")


class TestBaseModel:
    def test_model_has_mixins(self):
        class ObjectWithTimestampsAndUuid(BaseModel):
            class Meta:  # type: ignore
                app_label = "base"

        obj = ObjectWithTimestampsAndUuid()
        for field in ("uuid", "created_at", "modified_at"):
            assert hasattr(obj, field)
